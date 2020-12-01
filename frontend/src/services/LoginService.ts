import { User } from '@/models/User';
import axios, { AxiosResponse } from 'axios';

import DataService from '../services/DataService';

export default class LoginService {

    public static async authenticateUser(username: string, password: string): Promise<AxiosResponse<any>> {
        return await axios.post('http://imac-van-pieter.local:4000/valid', {
            username: username, 
            password: password
        }).catch(error => {
            return error;
        });
    }

    public static logoutUser(): void {
        DataService.removeData();
    }

    public static isUserLoggedIn(): boolean {
        if(DataService.getUserData() !== null){
            return true;
        } else {
            return false;
        }
    }

    public static getUserData(): User {
        const user: User = {
            id: JSON.parse(DataService.getUserData()).id,
            username: JSON.parse(DataService.getUserData()).username
        }
        
        return user;
    }
}