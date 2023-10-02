from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Мокап базы данных заметок (в реальном приложении используйте базу данных)
notes = []

@app.route("/")
def index():
    return render_template("notes.html")

@app.route("/add", methods=["POST"])
def add_note():
    data = request.get_json()
    title = data.get("title")
    message = data.get("message")
    timestamp = "Здесь должна быть дата/время"  # Замените на реальную дату/время
    note = {"id": len(notes) + 1, "title": title, "message": message, "timestamp": timestamp}
    notes.append(note)
    return jsonify({"message": "Заметка успешно добавлена"})

@app.route("/list", methods=["GET"])
def list_notes():
    date = request.args.get("date")
    filtered_notes = [note for note in notes if date in note["timestamp"]]
    return jsonify(filtered_notes)

# Добавьте обработчики для чтения, редактирования и удаления заметок

if __name__ == "__main__":
    app.run(debug=True)
