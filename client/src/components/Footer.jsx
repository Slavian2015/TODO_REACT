import React from "react";
import Alert from "react-bootstrap/Alert";

function Footer() {
    return (
        <div className="footer">
            <footer class="py-1 bg-dark fixed-bottom">
                <Alert variant="danger">
                    <Alert.Heading>Внимание!</Alert.Heading>
                    <p>
                        Ваш TODO LIST будет автоматически очищаться демоном каждые 2 минуты
                    </p>
                </Alert>
                <div class="container">
                    <p class="m-0 text-center text-white">
                        Copyright
                    </p>
                </div>
            </footer>
        </div>
    );
}

export default Footer;