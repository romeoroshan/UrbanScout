
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
            $('#dateofbirth').change(function(){
                TDate();
            });
        });

        function validateName(fieldId) {
            var name = $(fieldId).val();
            console.log(name)

            var lettersWithSpaces = /^[A-Za-z\s]+$/;
            if (name.trim() === "") {
                console.log("entered")
                $("#fname").html("Enter the Name").css("color", "red");
            } else if (!lettersWithSpaces.test(name)) {
                $("#fname").html("Name field required only alphabet characters with spaces").css("color", "red");
            } else {
                $("#fname").html("");
            }
        }

        function validateName2(fieldId) {
            var name = $(fieldId).val();
            var lettersWithSpaces = /^[A-Za-z\s]+$/;
            if (name.trim() === "") {
                $("#lname").html("Enter the Name").css("color", "red");
            } else if (!lettersWithSpaces.test(name)) {
                $("#lname").html("Name field required only alphabet characters with spaces").css("color", "red");
            } else {
                $("#lname").html("");
            }
        }


        function validateEmail(fieldId) {
            var email = $(fieldId).val();
            var filter = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
            if (email === "") {
                $("#email").html("Enter the Email Id").css("color", "red");
            } else if (!filter.test(email)) {
                $("#email").html("Use correct Email Id").css("color", "red");
            } else {
                $("#email").html("");
            }
        }

        function validatePassword(fieldId) {
            var password = $(fieldId).val();
            var pwd_expression = /^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-])/;
            if (password === "") {
                $("#pass1").html("Enter the Password").css("color", "red");
            }else if(!pwd_expression.test(password))
                    {
                        $("#pass1").html("Use password with atleast one capital and small alphabets, special character and letters").css("color", "red");
                    }
            else 
            {
                $("#pass1").html("");
            }
        }

        function validateConfirmPassword(fieldId) {
            var password = $("#pass").val();
            var confirmPassword = $(fieldId).val();
            if (confirmPassword === "") {
                $("#cpass1").html("Enter the Confirm Password").css("color", "red");
            } else if (confirmPassword !== password) {
                $("#cpass1").html("Password do not match").css("color", "red");
            } else {
                $("#cpass1").html("");
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
            console.log("Working");
            var UserDate = document.getElementById("dateofbirth").value;
            var UserDate = new Date(UserDate);
            var ToDate = new Date(2016, 0, 1); 
            console.log(ToDate>UserDate) // Changed month to 0 (January)
            
            if (UserDate>ToDate) {
                $("#dob").html("You must be born before 2016").css("color", "red");
                console.log('in')
                return false;
            }
            return true;
        }