import axios, { AxiosResponse } from 'axios';

import DataService from '../services/DataService';

export default class LoginService {

    public static async authenticateUser(username: string, password: string): Promise<AxiosResponse<any>> {
        return await axios.post('http://imac-van-pieter.local:4000/valid', {
            username: username, 
            password: password
        });
    }

    public static isUserLoggedIn(): boolean {
        if(DataService.getUserData()){
            return true;
        } else {
            return false;
        }
    }
}