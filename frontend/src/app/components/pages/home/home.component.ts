import { Component, OnInit, OnDestroy } from '@angular/core';
import { Subscription } from 'rxjs';

import { Post } from '../../../models/post.model'
import { PostService } from '../../../services/post.service'

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit, OnDestroy{
  posts: Post[] = [];
  private postSubscribe: Subscription;

  constructor(public postService: PostService){}

  ngOnInit(){
    this.postService.getPosts();
    this.postSubscribe = this.postService.getPostsUpdateListener()
      .subscribe((posts: Post[]) =>{
        this.posts = posts;
      });
  }

  ngOnDestroy(){
    this.postSubscribe.unsubscribe();
  }

}
