import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';
import {Comment} from '../interfaces/comment';
import {tap} from 'rxjs/operators';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class CommentService {

  constructor(private http:HttpClient) { }
  commentUrl=`http://${environment.backend_host}:${environment.backend_ip}/nchan/comments/`;

  addComment(comment):Observable<Comment>{
    return this.http.post<Comment>(`${this.commentUrl}`,comment).pipe(
      tap((x => {
        console.log(`added ${x}`)
      }))
    )
  }
}
