import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';
import {BoardsContext} from '../interfaces/boards-context';
import {Board} from '../interfaces/board';
import { environment } from '../../environments/environment';


@Injectable({
  providedIn: 'root'
})
export class BoardsService {

  constructor(private http: HttpClient) {
  }



  private appUrl=`http://${environment.backend_host}:${environment.backend_ip}/nchan/boards/`;

  getBoards(): Observable<BoardsContext> {
    return this.http.get<BoardsContext>(`${this.appUrl}?format=json`);
  }


  getBoard(id): Observable<Board> {
    return this.http.get<Board>(`${this.appUrl}${id}?format=json`);
  }
}
