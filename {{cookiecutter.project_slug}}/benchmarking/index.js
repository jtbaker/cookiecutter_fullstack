import http from 'k6/http';
import { sleep } from 'k6';

export const ROUTE = "http://localhost/model/testmodel"

export function buildRandomObject(){
    return {
        a: Math.random() * 2, b: Math.random() * 5, c: Math.random() * 3
    }
}

export function makeBody(){
    return Array.from({length: 10}, buildRandomObject)
}

export default function() {
    const response = http.post(ROUTE, JSON.stringify(makeBody()), {headers: {"Content-Type": "application/json"}})
    console.log(response.json().slice(0,10))
}