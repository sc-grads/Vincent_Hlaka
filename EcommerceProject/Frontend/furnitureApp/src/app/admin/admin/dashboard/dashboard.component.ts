import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  // Component properties

  constructor(private http: HttpClient) { }

  ngOnInit() {
  // Fetch initial data from the server
  this.http.get('/api/admin/dashboard').subscribe(
    (data) => {
      // Handle successful response
      console.log(data);
    },
    (error) => {
      // Handle error response
      console.error(error);
    }
  );
}
}
