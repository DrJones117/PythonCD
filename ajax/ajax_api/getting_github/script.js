async function getCoderData() {
        var response = await fetch("https://api.github.com/users/DrJones117");
        var coderData = await response.json();
        return coderData;
    }
        
    console.log(getCoderData());
    