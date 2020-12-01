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
            <footer>Bill Gates</footer>
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
                                <p>Added the Raspberry Pi camera module. This camera is used to take photos and videos so the user can see what activities take place at their house. <br><br>
                            </p>
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
                                <p>Added the Arduino UNO R3. With the Arduino we give ourselves the oppurtunity to read analog and digital sensors. With this functionality the security 
                                    system can be triggered. <br><br>
                                </p>
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
                                <p>Added some sensors. Currenty a distance sensor and LDR have been added. The distance sensor is used to trigger the security system. The LDR is used to 
                                    give the user some trivial information about the light intensity.
                                </p>
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
                                <p>The dashboard is added. The dashboard gives the user insight in the security system. This is the place where the user can see what activities there 
                                    have been and when. The dashboard also provides sensor information.
                                </p>
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

<div class="uk-section uk-background-primary">
    <div class="uk-container ">
    <span class="uk-label uk-margin-bottom uk-background-secondary">Iteration #2</span>
        <div uk-slider="center: true">

            <div class="uk-position-relative uk-visible-toggle uk-light" tabindex="-1">

                <ul class="uk-slider-items uk-child-width-1-2@s uk-grid">
                    <li>
                        <div class="uk-card uk-card-default">
                            <div class="uk-card-media-top">
                                <img src="img/product-it2.jpg" alt="">
                            </div>
                            <div class="uk-card-body">
                                <h3 class="uk-card-title">PIR sensor</h3>
                                <p>Added the PIR sensor. The PIR sensor is used to validate the activities even more. The system now added a restriction to the recording of the security 
                                    camera. Now the system has to also detect an infrared signal before the camera takes a video.
                            </p>
                            </div>
                        </div>
                    </li>
                    <li>
                        <div class="uk-card uk-card-default">
                            <div class="uk-card-media-top">
                                <img src="img/deep-learning.jpg" alt="">
                            </div>
                            <div class="uk-card-body">
                                <h3 class="uk-card-title">Deep Learning</h3>
                                <p>Started deep learning development. Deep learning will be used for recognizing human beings. This prevents the system from recording unnecessary events,
                                    like the passing of a dog. <br><br>
                                </p>
                            </div>
                        </div>
                    </li>
                    <li>
                        <div class="uk-card uk-card-default">
                            <div class="uk-card-media-top">
                                <img src="img/product-it2.jpg" alt="">
                            </div>
                            <div class="uk-card-body">
                                <h3 class="uk-card-title">Sensors</h3>
                                <p>Added some sensors. Currenty a distance sensor and LDR have been added. The distance sensor is used to trigger the security system. The LDR is used to 
                                    give the user some trivial information about the light intensity.
                                </p>
                            </div>
                        </div>
                    </li>
                    <li>
                        <div class="uk-card uk-card-default">
                            <div class="uk-card-media-top">
                                <img src="img/product-it2.jpg" alt="">
                            </div>
                            <div class="uk-card-body">
                                <h3 class="uk-card-title">Dashboard</h3>
                                <p>The dashboard is added. The dashboard gives the user insight in the security system. This is the place where the user can see what activities there 
                                    have been and when. The dashboard also provides sensor information.
                                </p>
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