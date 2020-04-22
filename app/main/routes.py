from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, g
from flask_login import current_user, login_required
from flask_babel import _, get_locale
from app import current_app, db
from app.main.forms import EditProfileForm, PostForm, InfoEditionsForm, InfoEditionsDESCForm, CloudServiceForm, \
    MainProductForm
from app.models import User, Post, InfoEditions, InfoEditions_desc, CloudService, MainProduct
from app.main import bp
from functools import wraps


@bp.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()
    g.locale = str(get_locale())


def is_admin(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        try:
            if current_user.username == 'admin':
                return func(*args, **kwargs)
            else:
                raise
        except:
            return render_template('errors/404.html'), 404

    return decorated_view


@bp.route('/', methods=['GET', 'POST'])
def home():
    ads = MainProduct.query.all()
    return render_template('home.html',ads=ads)

@bp.route('/product', methods=['GET', 'POST'])
def product():
    return render_template('product.html')
@bp.route('/cloud', methods=['GET', 'POST'])
def cloud():
    return render_template('cloud.html')
@bp.route('/services', methods=['GET', 'POST'])
def services():
    return render_template('services.html')

@bp.route('/forum', methods=['GET', 'POST'])
@login_required
def forum():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(body=form.post.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash(_('Your post is now live!'))
        return redirect(url_for('main.forum'))
    page = request.args.get('page', 1, type=int)
    posts = current_user.followed_posts().paginate(
        page, current_app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('main.forum', page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('main.forum', page=posts.prev_num) \
        if posts.has_prev else None
    return render_template('forum.html', title=_('Forum'), form=form,
                           posts=posts.items, next_url=next_url,
                           prev_url=prev_url)


@bp.route('/explore')
@login_required
def explore():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.timestamp.desc()).paginate(
        page, current_app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('main.explore', page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('main.explore', page=posts.prev_num) \
        if posts.has_prev else None
    return render_template('forum.html', title=_('Explore'),
                           posts=posts.items, next_url=next_url,
                           prev_url=prev_url)


@bp.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    page = request.args.get('page', 1, type=int)
    posts = user.posts.order_by(Post.timestamp.desc()).paginate(
        page, current_app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('main.user', username=user.username, page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('main.user', username=user.username, page=posts.prev_num) \
        if posts.has_prev else None
    return render_template('user.html', user=user, posts=posts.items,
                           next_url=next_url, prev_url=prev_url)


@bp.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash(_('Your changes have been saved.'))
        return redirect(url_for('main.edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title=_('Edit Profile'),
                           form=form)


@bp.route('/follow/<username>')
@login_required
def follow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash(_('User %(username)s not found.', username=username))
        return redirect(url_for('main.forum'))
    if user == current_user:
        flash(_('You cannot follow yourself!'))
        return redirect(url_for('main.user', username=username))
    current_user.follow(user)
    db.session.commit()
    flash(_('You are following %(username)s!', username=username))
    return redirect(url_for('main.user', username=username))


@bp.route('/unfollow/<username>')
@login_required
def unfollow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash(_('User %(username)s not found.', username=username))
        return redirect(url_for('main.forum'))
    if user == current_user:
        flash(_('You cannot unfollow yourself!'))
        return redirect(url_for('main.user', username=username))
    current_user.unfollow(user)
    db.session.commit()
    flash(_('You are not following %(username)s.', username=username))
    return redirect(url_for('main.user', username=username))





# admin功能
@bp.route('/database_index', methods=['GET', 'POST'])
@is_admin
def database_index():
    return render_template('DatabaseIndex.html')

@bp.route('/info_editions', methods=['GET', 'POST'])
@is_admin
def edition_form():
    form = InfoEditionsForm()
    editions = InfoEditions.query.all()
    if form.validate_on_submit():
        edition = InfoEditions(title=form.title.data, content=form.content.data)
        db.session.add(edition)
        db.session.commit()
        flash(_('Added'))
        return redirect(url_for('main.edition_form'))
    if request.method == 'POST':
        del_form = request.form
        for ID in del_form.to_dict():
            record_id = ID
        del_edition = InfoEditions.query.filter_by(id=record_id).first()
        db.session.delete(del_edition)
        db.session.commit()
        flash(_('Deleted'))
        return redirect(url_for('main.edition_form'))
    return render_template('InfoEditionsForm.html', form=form, editions=editions)


@bp.route('/info_editions/<data_id>', methods=['GET', 'POST'])
@is_admin
def edition_form_id(data_id):
    form = InfoEditionsForm()
    edition = InfoEditions.query.filter_by(id=data_id).first()
    if form.validate_on_submit():
        edition.title = form.title.data
        edition.content = form.content.data
        db.session.commit()
        flash(_('Updated'))
        return redirect(url_for('main.edition_form'))
    return render_template('InfoEditionsForm.html', form=form, edition=edition, update=True)


@bp.route('/info_editions_description', methods=['GET', 'POST'])
@is_admin
def edition_desc_form():
    form = InfoEditionsDESCForm()
    descriptions = InfoEditions_desc.query.all()
    if form.validate_on_submit():
        description = InfoEditions_desc(title=form.title.data, content=form.content.data,
                                        edition_id=form.edition_id.data)
        db.session.add(description)
        db.session.commit()
        flash(_('Added'))
        return redirect(url_for('main.edition_desc_form'))
    if request.method == 'POST':
        del_form = request.form
        for ID in del_form.to_dict():
            record_id = ID
        del_edition_desc = InfoEditions_desc.query.filter_by(id=record_id).first()
        db.session.delete(del_edition_desc)
        db.session.commit()
        flash(_('Deleted'))
        return redirect(url_for('main.edition_desc_form'))
    return render_template('InfoEditionsDescription.html', form=form, descriptions=descriptions)


@bp.route('/info_editions_description/<data_id>', methods=['GET', 'POST'])
@is_admin
def edition_desc_form_id(data_id):
    form = InfoEditionsDESCForm()
    description = InfoEditions.query.filter_by(id=data_id).first()
    if form.validate_on_submit():
        description.title = form.title.data
        description.content = form.content.data
        description.edition_id = form.edition_id.data
        db.session.commit()
        flash(_('Updated'))
        return redirect(url_for('main.edition_desc_form'))
    return render_template('InfoEditionsDescription.html', form=form, description=description, update=True)


@bp.route('/info_cloudservice', methods=['GET', 'POST'])
@is_admin
def cloudservice_form():
    form = CloudServiceForm()
    services = CloudService.query.all()
    if form.validate_on_submit():
        service = CloudService(title=form.title.data, content=form.content.data)
        db.session.add(service)
        db.session.commit()
        flash(_('Added'))
        return redirect(url_for('main.cloudservice_form'))
    if request.method == 'POST':
        del_form = request.form
        for ID in del_form.to_dict():
            record_id = ID
        del_service = CloudService.query.filter_by(id=record_id).first()
        db.session.delete(del_service)
        db.session.commit()
        flash(_('Deleted'))
        return redirect(url_for('main.cloudservice_form'))
    return render_template('InfoCloudService.html', form=form, services=services)


@bp.route('/info_cloudservice/<data_id>', methods=['GET', 'POST'])
@is_admin
def cloudservice_form_id(data_id):
    form = CloudServiceForm()
    service = CloudService.query.filter_by(id=data_id).first()
    if form.validate_on_submit():
        service.title = form.title.data
        service.content = form.content.data
        db.session.commit()
        flash(_('Updated'))
        return redirect(url_for('main.cloudservice_form'))
    return render_template('InfoCloudService.html', form=form, service=service, update=True)


@bp.route('/main_product', methods=['GET', 'POST'])
@is_admin
def info_main_productForm():
    form = MainProductForm()
    mainproducts = MainProduct.query.all()
    if form.validate_on_submit():
        mainproduct = MainProduct(title=form.title.data, intro=form.intro.data,
                                        url=form.url.data,icon=form.icon.data)
        db.session.add(mainproduct)
        db.session.commit()
        flash(_('Added'))
        return redirect(url_for('main.info_main_productForm'))
    if request.method == 'POST':
        del_form = request.form
        for ID in del_form.to_dict():
            record_id = ID
        del_mainproduct = MainProduct.query.filter_by(id=record_id).first()
        db.session.delete(del_mainproduct)
        db.session.commit()
        flash(_('Deleted'))
        return redirect(url_for('main.info_main_productForm'))
    return render_template('InfoMainProductForm.html', form=form, mainproducts=mainproducts)
@bp.route('/main_product/<data_id>', methods=['GET', 'POST'])
@is_admin
def info_main_productForm_id(data_id):
    form = MainProductForm()
    mainproduct = MainProduct.query.filter_by(id=data_id).first()
    if form.validate_on_submit():
        mainproduct.title = form.title.data
        mainproduct.intro = form.intro.data
        mainproduct.url = form.url.data
        mainproduct.icon = form.icon.data
        db.session.commit()
        flash(_('Updated'))
        return redirect(url_for('main.info_main_productForm'))
    return render_template('InfoMainProductForm.html', form=form, mainproduct=mainproduct, update=True)