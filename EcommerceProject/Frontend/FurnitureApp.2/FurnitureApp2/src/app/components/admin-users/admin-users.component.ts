import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-admin-users',
  templateUrl: './admin-users.component.html',
  styleUrls: ['./admin-users.component.css']
})
export class AdminUsersComponent {
  customerId: number | null = null;

  constructor(private http: HttpClient) {}

  deleteUser() {
    if (!this.customerId) {
      console.error('No customerId specified.');
      return;
    }

    // Make an HTTP DELETE request to delete the user with the given customer_id
    this.http.delete(`/customer/${this.customerId}`).subscribe(
      () => {
        console.log('User deleted successfully');
        // Clear the input field after successful deletion
        this.customerId = null;
      },
      (error: any) => {
        console.error('Error deleting user:', error);
      }
    );
  }
}
