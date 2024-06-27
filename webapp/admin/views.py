from webapp.user.decorators import admin_required
from flask import Blueprint, render_template

blueprint = Blueprint('admin', __name__, url_prefix='/admin')


@blueprint.route('/')
@admin_required
def personal_area():
    title = 'Панель управления'
    return render_template('admin/index.html', page_title=title)


