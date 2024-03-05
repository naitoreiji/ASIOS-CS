function pressed() {
    var text = document.getElementById("inp").value;
    document.getElementById("inp").value = "";

    if (text === "hello" || text === "hi" || text === "hola") {
        document.getElementById("main").innerHTML = "Hello Sir!";
    }
    else if (text === "how are you" || text === "are you fine" || text === "how is it going") {
        document.getElementById("main").innerHTML = "I am fine Sir ! Thank You for asking.";
    }
    else if (text === "what is your name" || text === "who are you")
        document.getElementById("main").innerHTML = "My name is EDITH. I am a chatbot !";

    else {
        document.getElementById("main").innerHTML = "Sorry ! Wrong Command";
    }
}
Footer
© 2023 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
