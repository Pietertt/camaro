import axios from 'axios';

export default class LoginService {

    public static async authenticateUser(username: string, password: string) {
        return axios.post('http://imac-van-pieter.local:4000/valid', {
            username: username, 
            password: password
        });
    }
}