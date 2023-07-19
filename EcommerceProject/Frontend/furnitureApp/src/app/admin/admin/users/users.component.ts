import { Component } from '@angular/core';
import { Router } from '@angular/router';


@Component({
  selector: 'app-users',
  template: `
    <!-- Users component content -->
    <button (click)="deleteUser(userId)">Delete User</button>
  `
})
export class UsersComponent {
  userId: string = ''; // Assuming you have a way to obtain the user ID

  deleteUser(userId: string) {
    // Delete user logic
  }
}
