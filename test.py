<html lang="en">

<head>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script src="https://kit.fontawesome.com/bfed39071c.js" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.6.0/gsap.min.js"></script>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Book Recommendation</title>
</head>

<style>
    body {
        margin: 0;
        font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
    }


    ::-webkit-scrollbar {
        width: 15px;
    }

    ::-webkit-scrollbar-track {
        background: #f1f1f1;
    }

    ::-webkit-scrollbar-thumb {
        border-radius: 10px;
        background: #888;
    }

    ::-webkit-scrollbar-thumb:hover {
        background: #555;
    }

    nav {
        display: flex;
        z-index: 5;
        position: absolute;
        position: fixed;
        top: 0;
        background-color: rgb(44, 93, 95);
        border-bottom-left-radius: 5px;
        border-bottom-right-radius: 5px;
        width: 100%;
        height: 70px;
    }

    h2 {
        text-align: center;
    }

    .container-user {
        margin: 10px;
        display: grid;
        place-items: center;
    }

    .content {
        box-shadow: 2px 5px 12px cadetblue;
        background-color: rgb(241, 238, 238);
        border-radius: 5px;
        padding: 10px;
        border: 2px solid cadetblue;
        width: 750px;
        max-width: 90%;
    }

    .p {
        font-size: x-large;

        padding: 12px;
        color: white;
        transition: 0.2s all ease;
        background-color: rgb(91, 119, 132);
        border: 2px solid rgb(67, 113, 134);
        cursor: pointer;
        border-radius: 5px;
        display: grid;
        place-items: center;
        width: 150px;
        /* border: 2px solid cadetblue; */
        margin: 5px;
    }

    .p:hover {
        transition: 0.2s all ease;
        scale: 0.95;
    }

    .p:active {
        background-color: cadetblue;
    }

    .personalities {
        display: flex;
        flex-direction: column;
        place-items: center;
    }

    .circles {
        margin-top: 20px;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .content1 {
        display: block;
    }

    .books {
        display: grid;
        place-items: center;
    }

    .book {
        transition: 0.2s all ease;
        background-color: rgb(199, 217, 218);
        display: flex;
        border-radius: 3px;
        padding: 5px;
        height: 120px;
        margin: 5px;
        cursor: pointer;
        border: 2px solid gray;
        width: 90%;
    }

    .book:hover {
        transition: 0.2s all ease;
        scale: 0.99;
    }

    img {
        border: 2px solid darkgrey;
        border-radius: 5px;
        width: 100px;
        height: 120px;
    }

    .image {
        width: 100px;
    }

    .title-genre {
        width: 100%;
        display: grid;
        place-items: center;
    }

    .inp {
        transition: 0.5s all ease;
        cursor: pointer;
        font-weight: bold;
        padding: 5px;
        margin: 6px;
        height: 40px;
        display: grid;
        place-items: center;
        border: 2px solid rgb(44, 93, 95);
        border-radius: 5px;
    }

    .inp:hover {
        border-radius: 5px;
        transition: 0.2 all ease;
        border: 2px solid antiquewhite;
    }

    .inp:active {
        scale: 0.99;
    }

    .navs {
        color: antiquewhite;
        position: absolute;
        display: flex;
        right: 30;
    }

    .logo {
        letter-spacing: 2px;
        color: antiquewhite;
        position: absolute;
        left: 30;
    }

    i {
        color: antiquewhite;
        visibility: hidden;
        cursor: pointer;
        font-size: x-large;
        position: absolute;
        z-index: 100;
        right: 20;
        top: 15;
    }

    .hiddenOptions {
        display: none;
        right: 0;
        border-radius: 4px;
        color: white;
        position: absolute;
        background-color: rgb(60, 79, 80);
        height: 150px;
        width: 250px;
    }

    h4, h3{
        text-align: center;
    }

    .options {
        display: grid;
        place-items: center;
    }

    .options div {
        transition: 0.3s all ease;
        cursor: pointer;
        width: fit-content;
        padding: 5px;
        text-align: center;
    }

    .options div:hover {
        transition: 0.3s all ease;
        scale: 1.02;
    }

    .cross {
        cursor: pointer;
        transform: translate(90%, 20%);
    }

    .button {
        transition: 0.3s all ease;
        color: black;
        cursor: pointer;
        border-radius: 5px;
        background-color: turquoise;
        border: 2px solid rgb(60, 79, 80);
        width: 400px;
        height: 80px;
    }

    .button:hover {
        transition: 0.3s all ease;
        box-shadow: 2px 2px 20px 10px gray;
        border: 2px solid turquoise;
    }

    .button:active {
        scale: 0.99;
    }

    .btn-name {
        text-align: center;
    }

    @media (max-width:700px) {

        .content {
            width: 550px;
        }

        i {
            visibility: visible;
        }

        .navs {
            display: none;
        }

        .logo {
            font-size: small;
        }
    }
</style>

<body>
    <nav>
        <div class="logo">
            <h2>Book Recommendation</h2>
        </div>
        <div class="bardiv" id="bardiv">
            <i id="bar" class="fa-solid fa-bars"></i>
        </div>
        <div class="navs">
            <div class="inp" id="inp1">Submit Data</div>
            <div class="inp" id="inp2">Recommendations</div>
        </div>
        <div class="hiddenOptions" id="hiddenOptions">
            <br><br>
            <div class="options">
                <div>Submit Data</div>
                <br>
                <div>Recommendations</div>
            </div>
        </div>
    </nav>
    <br><br><br><br>

    <div class="container-user">
        <div class="content">
            <div class="content1">
                <h2>What type of personality would you describe yourself as?</h2>
                <div class="personalities">
                    <div class="p" id="p1">Introvert</div>
                    <div class="p" id="p2">Extovert</div>
                </div>
            </div>
            <hr>
            <div class="content2">
                <h3>Please select up to three of your favorite books from this list so that we can recommend books to you based on your choices.</h3>
                <div class="books">

                    <div class="book" id="book1">
                        <div class="image" id="image1">
                            <img src="https://tse2.mm.bing.net/th?id=OIP.tT6tBsjQq6RzVEjT-nHiXgHaHa&pid=Api&P=0"
                                id="i1" alt="preview">
                        </div>
                        <div class="title-genre">
                            <h4 class="title" id="title1">Book 1</h4>
                            <h4 class="genre" id="genre1">Genre: </h4>
                        </div>
                    </div>

                    <div class="book" id="book2">
                        <div class="image" id="image2">
                            <img id="i2" src="https://tse2.mm.bing.net/th?id=OIP.tT6tBsjQq6RzVEjT-nHiXgHaHa&pid=Api&P=0"
                                alt="preview">
                        </div>
                        <div class="title-genre">
                            <h4 class="title" id="title2">Book 2</h4>
                            <h4 class="genre" id="genre2">Genre: </h4>
                        </div>
                    </div>
                    
                    <div class="book" id="book3">
                        <div class="image" id="image3">
                            <img id="i3" src="https://tse2.mm.bing.net/th?id=OIP.tT6tBsjQq6RzVEjT-nHiXgHaHa&pid=Api&P=0"
                                alt="preview unavailable!">
                        </div>
                        <div class="title-genre">
                            <h4 class="title" id="title3">Book 3</h4>
                            <h4 class="genre" id="genre3">Genre: </h4>
                        </div>
                    </div>

                    <div class="book" id="book4">
                        <div class="image" id="image4">
                            <img id="i4" src="https://tse2.mm.bing.net/th?id=OIP.tT6tBsjQq6RzVEjT-nHiXgHaHa&pid=Api&P=0"
                                alt="preview">
                        </div>
                        <div class="title-genre">
                            <h4 class="title" id="title4">Book 4</h4>
                            <h4 class="genre" id="genre4">Genre: </h4>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <br>
        <div class="button" id="button">
            <h1 class="btn-name">Recommend</h1>
        </div>
    </div>

</body>
<script>

    get5booksdata()


    var introvert = document.getElementById("p1");
    var extrovert = document.getElementById("p2");

    introvert.addEventListener("click", () => {
        introvert.style.backgroundColor = "rgb(89, 220, 42)"
        extrovert.style.backgroundColor = ""
    });
    extrovert.addEventListener("click", () => {
        introvert.style.backgroundColor = ""
        extrovert.style.backgroundColor = "rgb(89, 220, 42)"
    });

    var dictionary = {}
    var titles = []

    {
        // Personality

        document.getElementById("p1").addEventListener("click", function () {
            var personality = this.innerHTML;
            dictionary["personality"] = personality;
            console.log(personality);
        });

        document.getElementById("p2").addEventListener("click", function () {
            var personality = this.innerHTML;
            dictionary["personality"] = personality;
            console.log(personality);
        });

    }

    for (let i = 1; i <= 4; i++) {
        let book = document.getElementById("book" + i);

        book.addEventListener("click", function () {
            if (titles.length === 3) {
                alert("You have already selected the maximum number of books (3)");
                return;
            }
            if (titles.length < 3){
                book.style.backgroundColor = "rgb(89, 220, 42)"
            }
            let title = this.getElementsByClassName("title")[0].innerHTML;
            titles.push(title);
        });
    }

    dictionary["books"] = titles;

    let btn = document.getElementById("button")
    btn.addEventListener("click", function () {

        console.log(dictionary)

        $.ajax({
            type: "POST",
            url: "/recommendation",
            data: JSON.stringify(dictionary),
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            success: function(response) {
                console.log("Success!");
            }
        });

    });

    function showHide(id) {

        var el = document.getElementById(id);
        if (el && el.style.display == 'block') {
            el.style.display = 'none';
        }
        else {
            el.style.display = 'block';
        }
    }

    function get5booksdata() {
        $.get("/").done(function (data) {
            
            books = document.getElementsByClassName("book")
            
            for (let i = 1; i <=4 ; i++) {
            
                book_title = ("title" + i)
                document.getElementById(book_title).innerHTML = data[i]["Title"]

                book_genre = ("genre" + i)
                document.getElementById(book_genre).innerHTML = "Genre : " + data[i]["genre"]

                book_image = ("i" + i)
                document.getElementById(book_image).setAttribute("src" , data[i]["image"])
                        
            }
        });
    }

    document.getElementById("bardiv").onclick = function () {
        showHide('hiddenOptions')
    }

</script>

</html>