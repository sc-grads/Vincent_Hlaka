import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import {Router} from "@angular/router";

@Component({
  selector: 'app-admin-dashboard',
  templateUrl: './admin-dashboard.component.html',
  styleUrls: ['./admin-dashboard.component.css']
})
export class AdminDashboardComponent implements OnInit {

  users: any[] = [];
  products: any[] = [];

  constructor(private http: HttpClient, private router: Router) { }

  deleteUser(userId: number): void {
    // Delete user logic here
  }

  deleteProduct(productId: number): void {
    // Delete product logic here
  }

  ngOnInit(): void {
    this.fetchUsers();
    this.fetchProducts();
  }

  fetchUsers(): void {
    this.http.get<any[]>('/api/users').subscribe(
      (response: any[]) => {
        this.users = response;
      },
      (error: any) => {
        console.error('Error fetching users:', error);
      }
    );
  }

  fetchProducts(): void {
    this.http.get<any[]>('/api/products').subscribe(
      (response: any[]) => {
        this.products = response;
      },
      (error: any) => {
        console.error('Error fetching products:', error);
      }
    );
  }
}
