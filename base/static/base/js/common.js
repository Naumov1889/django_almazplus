(function () {
    document.querySelectorAll(".vacancy__btn").forEach(item => {
        item.addEventListener("click", e => {
            let vacancy_name = item.closest(".vacancy").querySelector(".vacancy__title").innerHTML.toLowerCase();

            document.querySelector(".vacancy-form-placeholder-text").innerHTML = vacancy_name;
            document.querySelector(".vacancy-form-placeholder-input").value = vacancy_name;
        })
    })
}());
(function () {
    document.querySelectorAll(".js-callback-btn").forEach(btn => {
        btn.addEventListener("click", function (e) {
            e.preventDefault();

            let form = this.closest("form");

            let csrfValue = form.querySelector("input[name=csrfmiddlewaretoken]").value;
            let nameInput = form.querySelector("input[name=name]");
            let nameValue = nameInput.value;
            let isNameValid = validateName(nameValue);
            let phoneInput = form.querySelector("input[name=phone]");
            let phoneValue = phoneInput.value;
            let isPhoneValid = validatePhone(phoneValue);

            let isCheckboxValid = true;
            if (Boolean(form.querySelector(".checkbox"))) {
                let checkbox_object = form.querySelector('.checkbox');
                let checkbox_input = form.querySelector('.checkbox__input');
                isCheckboxValid = validateCheckbox(checkbox_input);
            }

            let vacancyValue = "—";
            let productValue = "—";
            let emailValue = "—";
            let isEmailValid = true;

            if (Boolean(form.querySelector("input[name=vacancy]"))) {
                vacancyValue = form.querySelector("input[name=vacancy]").value;
            }

            if (Boolean(form.querySelector("input[name=product]"))) {
                productValue = form.querySelector("input[name=product]").value;
            }

            if (Boolean(form.querySelector("input[name=email]"))) {
                let emailInput = form.querySelector("input[name=email]");
                emailValue = emailInput.value;
                isEmailValid = validateEmail(emailValue);
                if (!isEmailValid) inputErrorAnimation(emailInput);
            }


            if (!isNameValid) inputErrorAnimation(nameInput);
            if (!isPhoneValid) inputErrorAnimation(phoneInput);
            if (!isCheckboxValid) inputErrorAnimation(checkbox_object);

            let isFormValid = isNameValid && isPhoneValid && isCheckboxValid && isEmailValid;

            console.log(nameValue, phoneValue, emailValue, vacancyValue);
            if (isFormValid) {
                postAjax('/callback/record_callback/', {
                    csrfmiddlewaretoken: csrfValue,
                    name: nameValue,
                    phone: phoneValue,
                    email: emailValue,
                    vacancy: vacancyValue,
                    product: productValue,
                }, function (data) {
                    document.querySelector('.my-spinner').style.display = "none";
                    document.querySelector('.js-popbox-callback-result .title_h2').innerHTML = '<span class="text_color_primary">Спасибо, <br></span> ваша заявка отправлена';
                    popbox.open("popbox-callback-result")
                }, function (data) {
                    document.querySelector('.my-spinner').style.display = "none";
                    document.querySelector('.js-popbox-callback-result .title_h2').innerHTML = '<span class="text_color_primary">Ошибка!</span> Пожалуйста, перезагрузите страницу и попробуйте отправить запрос снова.';
                    popbox.open("popbox-callback-result")
                });
                form.reset();
                popbox.close(form.closest(".popbox"));
                document.querySelector('.my-spinner').style.display = "inline-block";
            }

        });
    });


    function validateName(inputNameValue) {
        let name_format = /^[A-Za-z\u0400-\u04FF\s]+$/;
        return !!inputNameValue.match(name_format);
    }

    function validatePhone(inputPhoneValue) {
        return !!(inputPhoneValue.length === 15);
    }

    function validateCheckbox(input) {
        return input.checked;
    }


    function validateEmail(inputEmailValue) {
        let mail_format = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
        return !!inputEmailValue.match(mail_format);
    }

    function inputErrorAnimation(input) {
        input.classList.add("bounce");
        setTimeout(function () {
            input.classList.remove("bounce");
        }, 1000);
    }

    function postAjax(url, data, success, fail) {
        let params = typeof data == 'string' ? data : Object.keys(data).map(
            function (k) {
                return encodeURIComponent(k) + '=' + encodeURIComponent(data[k])
            }
        ).join('&');

        let xhr = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject("Microsoft.XMLHTTP");
        xhr.open('POST', url);
        xhr.onreadystatechange = function () {
            if (xhr.readyState > 3 && xhr.status === 200) {
                success(xhr.responseText);
            } else {
                fail(xhr.responseText)
            }
        };
        xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        xhr.send(params);
        return xhr;
    }

    let popbox = new Popbox();
}());

(function () {
    if (Boolean(document.querySelector('input[name=phone]'))) {
        document.querySelectorAll("input[name=phone]").forEach(input => {
            input.addEventListener("input", mask, false);
            input.addEventListener("focus", mask, false);
            input.addEventListener("blur", mask, false);
        });
    }

    function setCursorPosition(pos, elem) {
        elem.focus();
        if (elem.setSelectionRange) elem.setSelectionRange(pos, pos);
        else if (elem.createTextRange) {
            let range = elem.createTextRange();
            range.collapse(true);
            range.moveEnd("character", pos);
            range.moveStart("character", pos);
            range.select();
        }
    }

    function mask(event) {
        let matrix = "_ ___ ___ __ __",
            i = 0,
            def = matrix.replace(/\D/g, ""),
            val = this.value.replace(/\D/g, "");
        if (def.length >= val.length) val = def;
        this.value = matrix.replace(/./g, function (a) {
            return /[_\d]/.test(a) && i < val.length
                ? val.charAt(i++)
                : i >= val.length ? "" : a;
        });
        if (event.type === "blur") {
            if (this.value.length === 2) this.value = "";
        } else setCursorPosition(this.value.length, this);
    }
})();
(function () {
    document.querySelector(".burger").addEventListener("click", function () {
        document.querySelector(".overlay").classList.add("overlay_active");
        document.querySelector(".sidebar").classList.add("sidebar_active");
        document.querySelector(".pusher").classList.add("pusher_active");
    });

    document.querySelector(".overlay").addEventListener("click", function () {
        document.querySelector(".overlay").classList.remove("overlay_active");
        document.querySelector(".pusher").classList.remove("pusher_active");
        document.querySelector(".sidebar").classList.remove("sidebar_active");
    });

    document.querySelectorAll(".js-sidebar-nav-item").forEach(nav_item => {
        nav_item.addEventListener("click", function () {
            document.querySelector(".overlay").classList.remove("overlay_active");
            document.querySelector(".pusher").classList.remove("pusher_active");
            document.querySelector(".sidebar").classList.remove("sidebar_active");
        });
    })
}());
(function () {
    if (Boolean(document.querySelector('.index-page-slider-section'))) {
        let n_of_slides = document.querySelectorAll('.index-page-slider__item').length;

        for (let i = 0; i < n_of_slides; i++) {
            let btn = document.createElement("button");
            document.querySelector('.index-page-slider__dots').appendChild(btn)
        }

        tns({
            "container": ".index-page-slider__item-list",
            "mouseDrag": true,
            "controlsContainer": ".index-page-slider__arrows",
            "navContainer": ".index-page-slider__dots",
        });
    }

    if (Boolean(document.querySelector('.js-gallery-slider'))) {
        if (window.innerWidth < 800) {
            tns({
                "container": ".js-gallery-slider",
                "mouseDrag": true,
                "navPosition": "bottom",
                "loop": false,
                "edgePadding": 20,
                "gutter": 10,
                // "items": 2,
                "fixedWidth": 130,
                responsive: {
                    740: {
                        "edgePadding": 20,
                        "fixedWidth": 204
                    },
                    490: {
                        "edgePadding": 20,
                        "fixedWidth": 160,
                        "gutter": 15,
                    },
                    360: {
                        "edgePadding": 20,
                        "fixedWidth": 140,
                        "gutter": 15,
                    },
                }
            });
        }
    }
}());