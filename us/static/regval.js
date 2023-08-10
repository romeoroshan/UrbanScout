
        $(document).ready(function () {
            $("#fn").keyup(function () {
                validateName("#fn");
            });

            $("#sn").keyup(function () {
                validateName2("#sn");
            });

            $("#mail").keyup(function () {
                validateEmail("#mail");
            });

            $("#pass").keyup(function () {
                validatePassword("#pass");
            });

            $("#cpass").keyup(function () {
                validateConfirmPassword("#cpass");
            });

            $("#number").keyup(function () {
                validatePhoneNumber("#number");
            });
        });

        function validateName(fieldId) {
            var name = $(fieldId).val();
            console.log(name)

            var lettersWithSpaces = /^[A-Za-z\s]+$/;
            if (name.trim() === "") {
                console.log("entered")
                $("#error").html("Enter the Name").css("color", "red");
            } else if (!lettersWithSpaces.test(name)) {
                $("#error").html("Name field required only alphabet characters with spaces").css("color", "red");
            } else {
                $("#error").html("");
            }
        }

        function validateName2(fieldId) {
            var name = $(fieldId).val();
            var lettersWithSpaces = /^[A-Za-z\s]+$/;
            if (name.trim() === "") {
                $("#error").html("Enter the Name").css("color", "red");
            } else if (!lettersWithSpaces.test(name)) {
                $("#error").html("Name field required only alphabet characters with spaces").css("color", "red");
            } else {
                $("#error").html("");
            }
        }


        function validateEmail(fieldId) {
            var email = $(fieldId).val();
            var filter = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
            if (email === "") {
                $("#error").html("Enter the Email Id").css("color", "red");
            } else if (!filter.test(email)) {
                $("#error").html("Use correct Email Id").css("color", "red");
            } else {
                $("#error").html("");
            }
        }

        function validatePassword(fieldId) {
            var password = $(fieldId).val();
            var pwd_expression = /^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-])/;
            if (password === "") {
                $("#error").html("Enter the Password").css("color", "red");
            }else if(!pwd_expression.test(password))
                    {
                        $("#error").html("Use password with atleast one capital and small alphabets, special character and letters").css("color", "red");
                    }
            else 
            {
                $("#error").html("");
            }
        }

        function validateConfirmPassword(fieldId) {
            var password = $("#pass").val();
            var confirmPassword = $(fieldId).val();
            if (confirmPassword === "") {
                $("#error").html("Enter the Confirm Password").css("color", "red");
            } else if (confirmPassword !== password) {
                $("#error").html("Password do not match").css("color", "red");
            } else {
                $("#error").html("");
            }
        }

        function validatePhoneNumber(fieldId) {
            var numberRegex = /^[-+]?\d*\.?\d+$/;
            var phoneNumber = $(fieldId).val();

            if (phoneNumber === "") {
                $("#error").html("Enter the Phone number").css("color", "red");
            } else if (!numberRegex.test(phoneNumber)) {
                $("#error").html("Invalid phone Number").css("color", "red");
            } else if (phoneNumber.length > 10) {
                $("#error").html("Use correct phone Number").css("color", "red");
            } else {
                $("#error").html("");
            }
        }


        function togglePasswordVisibility() {
            var passwordInput = document.getElementById("pass");
            var eyeIcon = document.getElementById("eyeIcon");

            if (passwordInput.type === "password") {
                passwordInput.type = "text";
                eyeIcon.classList.remove("fa-eye-slash");
                eyeIcon.classList.add("fa-eye");
            } else {
                passwordInput.type = "password";
                eyeIcon.classList.remove("fa-eye");
                eyeIcon.classList.add("fa-eye-slash");
            }
        }
        function togglecPasswordVisibility() {
            var passwordInput = document.getElementById("cpass");
            var eyeIcon = document.getElementById("eyeIcon2");

            if (passwordInput.type === "password") {
                passwordInput.type = "text";
                eyeIcon.classList.remove("fa-eye-slash");
                eyeIcon.classList.add("fa-eye");
            } else {
                passwordInput.type = "password";
                eyeIcon.classList.remove("fa-eye");
                eyeIcon.classList.add("fa-eye-slash");
            }
        }

        function TDate() {
            console.log("Entered")
            var UserDate = document.getElementById("dateofbirth").value;
            var ToDate = new Date(2016, 1, 1);
            console.log(UserDate,ToDate)
            if (new Date(UserDate).getTime() < ToDate.getTime()) {
                alert("The Date must be Bigger or Equal to today date");
                return false;
            }
            return true;
        }