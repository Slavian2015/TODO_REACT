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
        let {taskSlug} = this.props.params;
        axios.get("/api/todos/" + taskSlug)
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
        axios.patch('/api/todos/' + this.state.taskSlug, {title: this.state.setTaskTitle})
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