<html>
<head>
<!-- UIkit CSS -->
<link rel="stylesheet" href="css/uikit.rtl.min.css" />
<link rel="stylesheet" href="css/uikit.min.css" />

<!-- UIkit JS -->
<script src="js/uikit.min.js"></script>
<script src="js/uikit-icons.min.js"></script>
</head>
<body>
<nav class="uk-navbar-container" uk-navbar>
    <div class="uk-navbar-left">
        <ul class="uk-navbar-nav">
            <li class="uk-active"><a href="index.php">HOME</a></li>
            <li class="uk-parent"><a href="products.php">PRODUCTS</a></li>
            <li><a href="about.php">ABOUT US</a></li>
        </ul>
    </div>
</nav>

<div id="test-filter" class="uk-height-large uk-background-cover uk-overflow-hidden uk-flex uk-flex-top" uk-parallax="sepia: 100;" style="background-image: url('img/header.jpg');">

    <h1 class="uk-width-1-2@m uk-text-center uk-margin-auto uk-margin-auto-vertical" uk-parallax="target: #test-filter; blur: 0,10;">Camaro</h1>

</div>


<div class="uk-section">
    <div class="uk-container">
        <div class="uk-child-width-1-3@m" uk-grid uk-scrollspy="cls: uk-animation-slide-right; target: .uk-card; delay: 500; repeat: false">
            <div>
                <div class="uk-card uk-card-default uk-card-body">
                    <h3 class="uk-card-title">High quality camera</h3>
                    <p>Camaro has a high standard in camera quality. Because of the great camera it is not hard to identify the person standing in front of the camera.</p>
                </div>
            </div>
            <div>
                <div class="uk-card uk-card-default uk-card-body">
                    <h3 class="uk-card-title">Easy to use</h3>
                    <p>The camera is easily installed on your house. With our easy to use dashboard you will have no problems observing your security footage.</p>
                </div>
            </div>
            <div>
                <div class="uk-card uk-card-default uk-card-body">
                    <h3 class="uk-card-title">Privacy guaranteed</h3>
                    <p>We do not use your data without your permission. If you don't want to send us any user data, you don't have to. Your privacy is our number one concern.</p>
                </div>
            </div>  
        </div>
    </div>
</div>


<div class="uk-section">
    <div class="uk-container">
        <blockquote cite="#">
            <p class="uk-margin-small-bottom">The most secure camera security system that has ever been developed. This product is a real recommendation if you value your privacy and don't want to break the bank.</p>
            <footer>Someone famous in <cite><a href="#">Source Title</a></cite></footer>
        </blockquote>
    </div>
</div>

<div class="uk-section uk-background-muted">
    <div class="uk-container ">
    <span class="uk-label uk-margin-bottom">Iteration #1</span>
        <div uk-slider="center: true">

            <div class="uk-position-relative uk-visible-toggle uk-light" tabindex="-1">

                <ul class="uk-slider-items uk-child-width-1-2@s uk-grid">
                    <li>
                        <div class="uk-card uk-card-default">
                            <div class="uk-card-media-top">
                                <img src="img/pi-camera-it1.jpg" alt="">
                            </div>
                            <div class="uk-card-body">
                                <h3 class="uk-card-title">Raspberry Pi - Camera module</h3>
                                <p>The camera of the Raspberry Pi gives us the quality we need with the usability that we want.</p>
                            </div>
                        </div>
                    </li>
                    <li>
                        <div class="uk-card uk-card-default">
                            <div class="uk-card-media-top">
                                <img src="img/arduino-it1.jpg" alt="">
                            </div>
                            <div class="uk-card-body">
                                <h3 class="uk-card-title">Arduino UNO R3</h3>
                                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt.</p>
                            </div>
                        </div>
                    </li>
                    <li>
                        <div class="uk-card uk-card-default">
                            <div class="uk-card-media-top">
                                <img src="img/sensors-it1.jpg" alt="">
                            </div>
                            <div class="uk-card-body">
                                <h3 class="uk-card-title">Sensors</h3>
                                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt.</p>
                            </div>
                        </div>
                    </li>
                    <li>
                        <div class="uk-card uk-card-default">
                            <div class="uk-card-media-top">
                                <img src="img/dashboard-it1.jpg" alt="">
                            </div>
                            <div class="uk-card-body">
                                <h3 class="uk-card-title">Dashboard</h3>
                                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt.</p>
                            </div>
                        </div>
                    </li>
                </ul>

                <a class="uk-position-center-left uk-position-small uk-hidden-hover" href="#" uk-slidenav-previous uk-slider-item="previous"></a>
                <a class="uk-position-center-right uk-position-small uk-hidden-hover" href="#" uk-slidenav-next uk-slider-item="next"></a>

            </div>

            <ul class="uk-slider-nav uk-dotnav uk-flex-center uk-margin"></ul>

        </div>
    </div>
</div>

</body>
</html>