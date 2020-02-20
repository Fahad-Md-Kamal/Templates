import { Component, OnInit, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss']
})
export class HeaderComponent implements OnInit {

  @Output() toggleSideNav: EventEmitter<any> = new EventEmitter();
  @Output() Login: EventEmitter<any> = new EventEmitter();
  @Output() Logout: EventEmitter<any> = new EventEmitter();
  
  isVisible = false;

  constructor() { }

  ngOnInit() {
  }

  toggeleSideNav() {
    this.toggleSideNav.emit();
  }

  Authenticate() {
    this.Login.emit();
  }

  userLogout() {
    this.Logout.emit();
  }

}
