async function getCoderData() {
        var response = await fetch("https://api.github.com/users/DrJones117");
        var coderData = await response.json();
        console.log(coderData);
        console.log(Array.isArray(coderData));
        console.log(Array.isArray(coderData.email));

        var userName = document.getElementById("name");
        var profile = document.getElementById("profile");
        userName.innerHTML = `${coderData.login} has ${coderData.followers} followers`;
        profile.innerHTML = `<img src="${coderData.avatar_url}" alt="profile_image">`;
        return coderData;
    }

