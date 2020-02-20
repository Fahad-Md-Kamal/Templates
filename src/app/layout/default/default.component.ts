import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-default',
  templateUrl: './default.component.html',
  styleUrls: ['./default.component.scss']
})
export class DefaultComponent implements OnInit {

  isOpenedSideBar = true;
  isAuthenticated = true;

  constructor() { }

  ngOnInit() {
  }

  toggleSideNav() {
    this.isOpenedSideBar = !this.isOpenedSideBar;
  }

  onLogin() {
    this.isAuthenticated = true;
  }

  onLogout() {
    this.isAuthenticated = false;
  }

}
