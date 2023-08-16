from flask import Blueprint, render_template, request
from deep_translator import GoogleTranslator
from models.language_model import LanguageModel
# from models.history_model import HistoryModel


translate_controller = Blueprint("translate_controller", __name__)


# Reqs. 4 e 5
@translate_controller.route("/", methods=["GET", "POST"])
def index():
    all_languages = LanguageModel.list_dicts()
    translated_text = ''
    if request.form.get('text-to-translate'):
        translated_text = GoogleTranslator(
                source=request.form.get('translate-from'),
                target=request.form.get('translate-to'),
                ).translate(request.form.get('text-to-translate'))
    return render_template(
            "index.html",
            languages=all_languages,
            text_to_translate=request.form.get('text-to-translate'),
            translate_from={'acronym': request.form.get('translate-from')},
            translate_to={'acronym': request.form.get('translate-to')},
            translated=translated_text,
            )


# Req. 6
@translate_controller.route("/reverse", methods=["POST"])
def reverse():
    all_languages = LanguageModel.list_dicts()
    translated_text = GoogleTranslator(
            source=request.form.get('translate-from'),
            target=request.form.get('translate-to'),
            ).translate(request.form.get('text-to-translate'))
    return render_template(
            "index.html",
            languages=all_languages,
            text_to_translate=translated_text,
            translate_from={'acronym': request.form.get('translate-to')},
            translate_to={'acronym': request.form.get('translate-from')},
            translated=request.form.get('text-to-translate'),
            form=request.form,
            )
