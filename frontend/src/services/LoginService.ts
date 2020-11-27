import axios from 'axios';

export default class LoginService {

    public static async requestAuthentication(username: string, password: string) {
        return axios.post('http://imac-van-pieter.local:4000/valid', {
            username: username, 
            password: password}
        );
    }

    public static async authenticateUser(username: string, password: string) {
        const response = await LoginService.requestAuthentication(username, password).then(response => {
            if(response.status === 200){
                return true;
            } else {
                return false;
            }
        });
    }
}