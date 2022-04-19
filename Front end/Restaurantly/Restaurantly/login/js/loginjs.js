<script>
    var name1 = document.getElementById('name');
    var email = document.getElementById('email');
    var number = document.getElementById('number');
    var span = document.getElementsByTagName('span');
    var password = document.getElementById('password');
    var password1 = document.getElementById('password2');

    name1.onkeydown = function() {
        var nameregex = /^[A-Z\-]+[a-z\-]+$/;
        var uname = document.getElementById('name').value;
        document.getElementById('name').focus();

        if (uname == "") {

            span[0].innerText = "Name can'nt be blank";
            span[0].style.color = "red";
        } else if (uname.length < 8) {

            span[0].innerText = "Name can'nt be less than 8 character";
            span[0].style.color = "red";
        } else if (nameregex.test(uname)) {
            span[0].innerText = "your name is perfect!";
            span[0].style.color = "lime";
        } else if (/^[a-zA-Z0-9\-]+$/.test(uname)) {
            span[0].innerText = "your name is invalid";
            span[0].style.color = "red";
        } else {
            span[0].innerText = "Your name is Valid";
            span[0].style.color = "lime";
        }
    }
    email.onkeydown = function() {
        const regex1 = /^[a-z]+@([a-z]+)\.([a-z]{10,16})+\.[a-z]{1,2}$/;

        if (regex1.test(email.value)) {
            span[1].innerText = "Your Email is Valid";
            span[1].style.color = "lime";
        } else {
            span[1].innerText = "Invalid Email Id";
            span[1].style.color = "red";
        }
    }
    number.onkeydown = function() {
        const regnum = /^[0-9]{9}$/;
        if (regnum.test(number.value)) {
            span[2].innerText = "Your Number is Valid";
            span[2].style.color = "lime";
        } else {
            span[2].innerText = "Invalid Phone Number";
            span[2].style.color = "red";
        }
    }
    password.onkeydown = function() {
        var pass = document.getElementById('password').value;

        var pass1 = /^[a-zA-Z]{6,12}$/;
        var pass2 = /^[a-zA-Z0-9]{6,12}$/;
        var pass3 = /^[A-Z](?=.[0-9])(?=.[!@#$%^{}()&])[a-zA-Z0-9!@#$%{}()^&]{6,12}$/;
        if (pass.match(pass1)) {
            span[3].innerText = "Must include Digit(0-9)!";
            span[3].style.color = "red";
        } else if (pass.match(pass2)) {
            span[3].innerText = "Must include special character ~`!@#$%^&*()-_+={}[]|\;:";
            span[3].style.color = "red";
        } else if (pass.match(pass3)) { // && pass1.test(pass)) {
            span[3].innerText = "Strong passsword!";
            span[3].style.color = "lime";

        } else {
            span[3].innerText = "TRy Something new!";
            span[3].style.color = "red";
        }

    }
    password1.onkeydown = function() {
        var retype = document.getElementById('password2').value;
        var pass = document.getElementById('password').value;

        if (pass == retype) {
            span[4].innerText = "Password Matched";
            span[4].style.color = "lime";
        } else {
            span[4].innerText = "Password Must should be same!";
            span[4].style.color = "red";
        }
    }

    function validate() {
        if (document.getElementById('name').value == "") {
            document.getElementById('name').classList.add("color");
            alert('empty')

        }
        if (document.getElementById('email').value == "") {
            alert('Plzz fill email_id')
        }
    }
</script>