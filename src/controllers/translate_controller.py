from flask import Blueprint, render_template
# from deep_translator import GoogleTranslator
from models.language_model import LanguageModel
# from models.history_model import HistoryModel


translate_controller = Blueprint("translate_controller", __name__)


# Reqs. 4 e 5
@translate_controller.route("/", methods=["GET", "POST"])
def index():
    all_languages = LanguageModel.list_dicts()
    return render_template(
        "index.html",
        languages=all_languages,
        text_to_translate='',
        translate_from=all_languages[0],
        translate_to=all_languages[1],
        translated='',
        )


# Req. 6
@translate_controller.route("/reverse", methods=["POST"])
def reverse():
    raise NotImplementedError
