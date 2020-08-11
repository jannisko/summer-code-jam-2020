import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';
import {PostContext} from '../interfaces/post-context';
import {CommentsContext} from '../interfaces/comments-context';
import {Post} from '../interfaces/post';
import {tap} from 'rxjs/operators';
import { environment } from '../../environments/environment';


@Injectable({
  providedIn: 'root'
})
// @ts-ignore
export class PostsService {

  constructor(private _http: HttpClient) {
  }

  private boardsUrl = `http://${environment.backend_host}:${environment.backend_ip}/nchan/boards/`;
  private postsUrl = `http://${environment.backend_host}:${environment.backend_ip}/nchan/posts/`;

  getPostsForBoard(id): Observable<PostContext> {
    return this._http.get<PostContext>(`${this.boardsUrl}${id}/posts?format=json`);
  }

  getCommentsForPost(id): Observable<CommentsContext> {
    return this._http.get<CommentsContext>(`${this.postsUrl}${id}/comments?format=json`);
  }

  getPost(id): Observable<Post> {
    return this._http.get<Post>(`${this.postsUrl}${id}?format=json`);
  }

  addPost(post:Post):Observable<Post>{
    return this._http.post<Post>(`${this.postsUrl}`,post).pipe(
      tap((x)=>{
        console.log(`added ${x.title}`);
      })
    );
  }


}
