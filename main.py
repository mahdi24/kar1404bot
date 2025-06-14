from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Bot is running."

@app.route('/<token>', methods=['POST'])
def webhook(token):
    data = request.json
    message = data.get("message", {})
    text = message.get("text", "")
    chat_id = message.get("chat", {}).get("id")
    
    buttons = [
        ["🏖 مرخصی", "👴 بازنشستگی"],
        ["🔄 نقل و انتقالات", "📊 طبقه شغلی"],
        ["📈 رتبه شغلی", "💵 بازخرید"],
        ["📤 استعفا", "⚠️ تخلفات"],
        ["📃 گواهی اشتغال به کار", "📌 انتصابات"],
        ["📞 ارتباط با ما"]
    ]

    response_text = "به بازوی کارگزینی اداره آموزش و پرورش پاکدشت خوش آمدید."

    if text == "/start":
        reply_markup = {
            "keyboard": buttons,
            "resize_keyboard": True,
            "one_time_keyboard": False
        }
        return jsonify({
            "method": "sendMessage",
            "chat_id": chat_id,
            "text": response_text,
            "reply_markup": reply_markup
        })

    # پاسخ‌های ساده به دکمه‌ها
    responses = {
        "🏖 مرخصی": "راهنمای درخواست مرخصی: ...",
        "👴 بازنشستگی": "راهنمای بازنشستگی: ...",
        "🔄 نقل و انتقالات": "اطلاعات نقل و انتقالات: ...",
        "📊 طبقه شغلی": "طبقه شغلی چیست و چطور تعیین می‌شود؟ ...",
        "📈 رتبه شغلی": "راهنمای ارتقاء رتبه شغلی: ...",
        "💵 بازخرید": "شرایط بازخرید خدمت: ...",
        "📤 استعفا": "به زودی بارگذاری خواهد شد. از صبر و شکیبایی شما سپاسگزاریم.",
        "⚠️ تخلفات": "به زودی بارگذاری خواهد شد. از صبر و شکیبایی شما سپاسگزاریم.",
        "📃 گواهی اشتغال به کار": "به زودی بارگذاری خواهد شد. از صبر و شکیبایی شما سپاسگزاریم.",
        "📌 انتصابات": "آخرین اطلاعات انتصابات: ...",
        "📞 ارتباط با ما": "👤 مسئول کارگزینی: @Amir1068\n👤 مدیر سامانه: @teacher141072"
    }

    if text in responses:
        return jsonify({
            "method": "sendMessage",
            "chat_id": chat_id,
            "text": responses[text]
        })

    return jsonify({
        "method": "sendMessage",
        "chat_id": chat_id,
        "text": "دستور نامعتبر است. لطفاً از منوی زیر گزینه‌ای را انتخاب کنید."
    })