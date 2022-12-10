import React, {Component} from "react";
import axios from 'axios';
import {Button, Col, Container, Row} from 'react-bootstrap'

import {useParams} from "react-router-dom";

function withParams(Component) {
    return props => <Component {...props} params={useParams()}/>;
}

class Task extends Component {
    constructor(props) {
        super(props)
        this.state = {
            setTaskTitle: '',
            taskSlug: ''
        }
    }

    componentDidMount() {
        console.log("NEW PAGE")
        let {taskSlug} = this.props.params;
        axios.get("http://0.0.0.0:3232/todos/" + taskSlug, {
            "headers": {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET,PUT,POST,DELETE,PATCH,OPTIONS',
            }
        })
            .then((response) => {
                this.setState({
                    setTaskTitle: response.data.title,
                    taskSlug: taskSlug
                })
            })
    }

    handleChange = (event) => {
        let nam = event.target.name;
        let val = event.target.value
        this.setState({
            [nam]: val
        })
    }


    submit = () => {
        axios.patch('http://0.0.0.0:3232/todos/' + this.state.taskSlug, {title: this.state.setTaskTitle}, {
            "headers": {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET,PUT,POST,DELETE,PATCH,OPTIONS',
            }
        })
            .then((response) => {window.location.replace('/')})
    }

    render() {
        return (
            <div className='home'>
                <Container>
                    <Row>
                        <Col>
                            <Row>
                                <div className='form'>
                                    <input
                                        name='setTaskTitle'
                                        value={this.state.setTaskTitle}
                                        placeholder={this.state.setTaskTitle}
                                        onChange={this.handleChange}/>
                                </div>
                                <Button className='my-2' variant="primary" onClick={this.submit}>Save
                                    Changes</Button>
                                <Button className='my-2' variant="warning" href={"/"}>Cancel</Button>
                            </Row>
                        </Col>
                        <Col></Col>


                    </Row>

                    <br/><br/>
                </Container>
            </div>
        );
    }
}

export default withParams(Task);


// function
//
// Task() {
//     let {taskSlug} = useParams();
//
//     useEffect(() => {
//     }, [taskSlug]);
//
//     return (
//         <div className="home">
//             <div class="container">
//                 <h1 className="mt-5">This is a Task Title</h1>
//                 <h6 className="mb-5">The post slug is, {taskSlug}</h6>
//                 <p>
//                     Lorem Ipsum is simply dummy text of the printing and typesetting
//                     industry. Lorem Ipsum has been the industry's standard dummy text ever
//                     since the 1500s, when an unknown printer took a galley of type and
//                     scrambled it to make a type specimen book.
//                 </p>
//                 <p>
//                     Lorem Ipsum is simply dummy text of the printing and typesetting
//                     industry. Lorem Ipsum has been the industry's standard dummy text ever
//                     since the 1500s, when an unknown printer took a galley of type and
//                     scrambled it to make a type specimen book.
//                 </p>
//                 <p>
//                     Lorem Ipsum is simply dummy text of the printing and typesetting
//                     industry. Lorem Ipsum has been the industry's standard dummy text ever
//                     since the 1500s, when an unknown printer took a galley of type and
//                     scrambled it to make a type specimen book.
//                 </p>
//             </div>
//         </div>
//     );
// }