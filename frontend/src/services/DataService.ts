import { User } from '../models/User';

export default class DataService {

    public static setData(user: User): void {
        localStorage.setItem('user', JSON.stringify(user));
    }

    public static removeData(): void {
        localStorage.removeItem('user');
    }

    public static getUserData(): string {
        const data = localStorage.getItem('user');
        if(data !== null){
            return data;
        } 
        return '';
    }



}