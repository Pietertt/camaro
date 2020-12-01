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

    public static async getUserToken(id: number): Promise<AxiosResponse<any>> {
        return await axios.post('http://imac-van-pieter.local:4000/valid/token', {
            id: id
        }).catch(error => {
            return error;
        });
    }

    public static logoutUser(): void {
        DataService.removeData();
    }

    public static getUserData(): User {
        const user: User = {
            id: JSON.parse(DataService.getUserData()).id,
            username: JSON.parse(DataService.getUserData()).username,
            token: JSON.parse(DataService.getUserData()).token
        }
        
        return user;
    }
}