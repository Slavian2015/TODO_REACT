import React, {Component} from 'react';
import axios from 'axios';
import {Button, Container, Row, Col} from 'react-bootstrap'


class Home extends Component {
    constructor(props) {
        super(props)
        this.state = {
            setTaskTitle: '',
            fetchData: [],
        }
    }

    handleChange = (event) => {
        let nam = event.target.name;
        let val = event.target.value
        this.setState({
            [nam]: val
        })
    }

    componentDidMount() {
        axios.get("/api/todos",)
            .then((response) => {
                this.setState({
                    fetchData: response.data.tasks
                })
            })
    }

    submit = () => {
        axios.post('/api/todos', {title: this.state.setTaskTitle})
            .then((response) => {
                this.setState({
                    fetchData: this.state.fetchData.concat([response.data]),
                    setTaskTitle: ''
                });
            })
    }

    delete = (id) => {
        axios.delete(`/api/todos/${id}`)
        this.setState({
            fetchData: this.state.fetchData.filter(function (task) {
                return task.id !== id
            })
        });
    }

    render() {

        let card = this.state.fetchData.map((val, key) => {
            return (
                <React.Fragment>
                    <Row style={{marginBottom: "10px"}}>
                        <Col size={10}>{val.title}</Col>
                        <Col size={1}><Button size="sm" href={'/tasks/' + val.id}>Update</Button></Col>
                        <Col size={1}><Button variant="danger" size="sm" onClick={() => {
                            this.delete(val.id)
                        }}>Delete</Button></Col>
                    </Row>
                    <hr/>
                </React.Fragment>
            )
        })

        return (
            <div className='home'>

                <Container>
                    <h1>TO-DO List</h1>
                    <div className='form'>
                        <input name='setTaskTitle' placeholder='Enter New Task' onChange={this.handleChange}/>
                    </div>

                    <Button className='my-2' variant="primary" onClick={this.submit}>Submit</Button> <br/><br/>

                </Container>
                <Container class="first">
                    <Row>
                        {card}
                    </Row>
                </Container>
            </div>
        );
    }
}

export default Home;