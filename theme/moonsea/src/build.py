"""把 theme.css 打包成酒馆可导入的主题 JSON。
用法：python3 build.py  → 生成上一级目录里的 月光海·玻璃.json
"""
import json, pathlib

HERE = pathlib.Path(__file__).resolve().parent
CDN = "https://cdn.jsdelivr.net/gh/Ttsningning/orange-shop-assets@main/theme/moonsea/"

SETTINGS = {
    "name": "月光海·玻璃",
    "blur_strength": 0,
    "main_text_color": "rgba(43, 58, 110, 1)",
    "italics_text_color": "rgba(108, 123, 180, 1)",
    "underline_text_color": "rgba(77, 103, 191, 1)",
    "quote_text_color": "rgba(62, 92, 196, 1)",
    "blur_tint_color": "rgba(238, 242, 253, 0.97)",
    "chat_tint_color": "rgba(0, 0, 0, 0)",
    "user_mes_blur_tint_color": "rgba(0, 0, 0, 0)",
    "bot_mes_blur_tint_color": "rgba(0, 0, 0, 0)",
    "shadow_color": "rgba(0, 0, 0, 0)",
    "shadow_width": 0,
    "border_color": "rgba(0, 0, 0, 0)",
    "font_scale": 0.9,
    "fast_ui_mode": False,
    "waifuMode": False,
    "avatar_style": 0,
    "chat_display": 0,
    "toastr_position": "toast-top-center",
    "noShadows": True,
    "chat_width": 100,
    "timer_enabled": True,
    "timestamps_enabled": False,
    "timestamp_model_icon": False,
    "mesIDDisplay_enabled": True,
    "hideChatAvatars_enabled": False,
    "message_token_count_enabled": True,
    "expand_message_actions": False,
    "enableZenSliders": False,
    "enableLabMode": False,
    "hotswap_enabled": True,
    "bogus_folders": True,
    "zoomed_avatar_magnification": True,
    "reduced_motion": False,
    "compact_input_area": True,
    "show_swipe_num_all_messages": True,
    "click_to_edit": False,
    "media_display": "list",
}


def css(base: str) -> str:
    return (HERE / "theme.css").read_text(encoding="utf-8").replace("IMG/", base)


if __name__ == "__main__":
    data = dict(SETTINGS, custom_css=css(CDN))
    out = HERE.parent / "月光海·玻璃.json"
    out.write_text(json.dumps(data, ensure_ascii=False, indent=4), encoding="utf-8")
    print("wrote", out)
