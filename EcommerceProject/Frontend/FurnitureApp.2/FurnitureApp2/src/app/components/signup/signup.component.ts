import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.css']
})
export class SignupComponent {
  customer_email: string = '';
  first_name: string = '';
  last_name: string = '';
  password: string = '';
  address: string = '';
  postcode: string = '';
  city: string = '';
  phone: string = '';

  constructor(private http: HttpClient, private router: Router) { }

  onSubmit() {
    const data = {
      'customer_email': this.customer_email,
      'first_name': this.first_name,
      'last_name': this.last_name,
      'password': this.password,
      'address': this.address,
      'postcode': this.postcode,
      'city': this.city,
      'phone': this.phone,
    };

    this.http.post<any>('http://localhost:5000/signup', data).subscribe(
      response => {
        console.log(response);
        // handle success response here
        if (response.message === 'Done') {
          this.router.navigate(['/login']); // navigate to catalogue page
        } else {
          // handle invalid login
          // show an error message or perform any other necessary action
        }
      },
      error => {
        console.error(error);
        // handle error response here
        // show an error message or perform any other necessary action
      }
    );
  }
}

