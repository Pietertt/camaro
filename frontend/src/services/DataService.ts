import { User } from '../models/User';

export default class DataService {

    public static setData(user: User): void {
        localStorage.setItem('user', JSON.stringify(user));
    }

    public static getUserData(): boolean {
        const data = localStorage.getItem('user');
        if(data){
            return true;
        } else {
            return false;
        }
    }


}