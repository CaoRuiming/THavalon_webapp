import json
from collections import defaultdict
from flask import g, request, Markup, current_app, url_for
from werkzeug.local import LocalProxy

import os
from .helpers import env_is_dev


def parse_stats(f):
    """Parse Webpack JSON stats from a file-like object"""
    stats = json.load(f)
    all_assets = dict()
    for (chunk, entries) in stats["assetsByChunkName"].items():
        if not isinstance(entries, list):
            entries = [entries]
        assets = defaultdict(list)
        for entry in entries:
            _, ext = os.path.splitext(entry)
            if len(ext) > 0:
                assets[ext[1:]].append(entry)
        all_assets[chunk] = assets
    return all_assets


def _teardown_request(x):
    if hasattr(request, '_webpack_assets'):
        delattr(request, '_webpack_assets')


def _load_dev_stats():
    """Load the development stats.json"""
    stats = getattr(request, '_webpack_stats', None)
    if stats is None:
        stats_file = os.path.join(
            os.path.dirname(__file__), '..', '.dev-assets', 'stats.json')
        with open(stats_file) as f:
            stats = request._webpack_stats = parse_stats(f)
    return stats


def _dev_url_for(asset):
    webpack_port = os.environ.get('WEBPACK_PORT', '9999')
    return "http://localhost:{}/{}".format(webpack_port, asset)


def _load_prod_stats():
    """Load the production stats.json"""
    stats = getattr(g, '_webpack_stats', None)
    if stats is None:
        with current_app.open_resource('static/assets/stats.json') as f:
            stats = g._webpack_stats = parse_stats(f)
    return stats


def _prod_url_for(asset):
    return url_for('static', filename='assets/' + asset)


assets = LocalProxy(
    lambda: _load_dev_stats() if env_is_dev() else _load_prod_stats())


def init_webpack(app):
    with app.app_context():
        asset_url = _dev_url_for if env_is_dev() else _prod_url_for

        @app.template_global('assets')
        def require_assets(chunk_name):
            chunk_assets = assets.get(chunk_name, None)
            if chunk_assets is None:
                raise Exception(
                    'Unknown Webpack bundle: {}'.format(chunk_name))
            res = ""
            for js_file in chunk_assets.get('js', []):
                res += '<script src="{}"></script>\n'.format(
                    asset_url(js_file))
            for css_file in chunk_assets.get('css', []):
                res += '<link rel="stylesheet" href="{}">\n'.format(
                    asset_url(css_file))
            return Markup(res)

        if env_is_dev():
            app.teardown_request(_teardown_request)
