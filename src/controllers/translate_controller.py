from flask import Blueprint, render_template, request
from deep_translator import GoogleTranslator
from models.language_model import LanguageModel
from models.history_model import HistoryModel


translate_controller = Blueprint("translate_controller", __name__)


@translate_controller.route("/", methods=["GET", "POST"])
def index():
    all_languages = LanguageModel.list_dicts()
    translated_text = ''
    translate_req = request.form.get('text-to-translate')
    text_to_translate = translate_req if translate_req else ''
    if translate_req:
        translated_text = GoogleTranslator(
                source=request.form.get('translate-from'),
                target=request.form.get('translate-to'),
                ).translate(translate_req)
        HistoryModel({
            'text_to_translate': text_to_translate,
            'translate_from': request.form.get('translate-from'),
            'translate_to': request.form.get('translate-to'),
        }).save()
    return render_template(
            "index.html",
            languages=all_languages,
            text_to_translate=text_to_translate,
            translate_from={'acronym': request.form.get('translate-from')},
            translate_to={'acronym': request.form.get('translate-to')},
            translated=translated_text,
            )


@translate_controller.route("/reverse", methods=["POST"])
def reverse():
    all_languages = LanguageModel.list_dicts()
    translate_req = request.form.get('text-to-translate')
    translated_text = GoogleTranslator(
            source=request.form.get('translate-from'),
            target=request.form.get('translate-to'),
            ).translate(translate_req)
    HistoryModel({
            'text_to_translate': translate_req,
            'translate_from': request.form.get('translate-from'),
            'translate_to': request.form.get('translate-to'),
        }).save()
    return render_template(
            "index.html",
            languages=all_languages,
            text_to_translate=translated_text,
            translate_from={'acronym': request.form.get('translate-to')},
            translate_to={'acronym': request.form.get('translate-from')},
            translated=translate_req,
            form=request.form,
            )
