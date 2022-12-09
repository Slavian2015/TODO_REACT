import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import * as serviceWorker from "./serviceWorker";
import {BrowserRouter as Router, Route, Routes} from "react-router-dom";
import {Navigation, Footer, Home, Task} from "./components";
import 'bootstrap/dist/css/bootstrap.min.css';

ReactDOM.render(
    <Router>
        <Navigation/>
        <Routes>
            <Route path="/" element={<Home/>}/>
            <Route path="/tasks/:taskSlug" element={<Task/>}/>
        </Routes>
        <Footer/>
    </Router>,

    document.getElementById("root")
);

serviceWorker.unregister();