// static/courses_app/script.js

// Показываем уведомление
document.getElementById("registration-notification").style.display = "block";

// Закрываем уведомление при нажатии на крестик
document.getElementById("close-notification").onclick = function() {
    document.getElementById("registration-notification").style.display = "none";
};