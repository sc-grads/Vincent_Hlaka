import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-admin-products',
  templateUrl: './admin-products.component.html',
  styleUrls: ['./admin-products.component.css']
})
export class AdminProductsComponent {
  products: any[] = [];
  newProduct: any = {};
  editingProduct: any = null;

  constructor(private http: HttpClient) {}

  ngOnInit(): void {
    this.fetchProducts();
  }

  fetchProducts(): void {
    this.http.get('/api/products').subscribe(
      (response: any) => {
        this.products = response;
      },
      (error: any) => {
        console.error('Error fetching products:', error);
      }
    );
  }

  addProduct(): void {
    this.http.post('/api/products', this.newProduct).subscribe(
      () => {
        console.log('Product added successfully');
        this.newProduct = {}; // Clear the newProduct object
        this.fetchProducts(); // Fetch updated products list
      },
      (error: any) => {
        console.error('Error adding product:', error);
      }
    );
  }

  deleteProduct(productId: number): void {
    this.http.delete(`/api/products/${productId}`).subscribe(
      () => {
        console.log('Product deleted successfully');
        this.fetchProducts(); // Fetch updated products list
      },
      (error: any) => {
        console.error('Error deleting product:', error);
      }
    );
  }

  startEdit(product: any): void {
    this.editingProduct = { ...product }; // Create a copy of the product for editing
  }

  updateProduct(): void {
    if (!this.editingProduct) {
      console.error('No product is being edited.');
      return;
    }

    const { product_id, ...updatedProduct } = this.editingProduct;

    this.http.put(`/api/products/${product_id}`, updatedProduct).subscribe(
      () => {
        console.log('Product updated successfully');
        this.editingProduct = null; // Clear the editingProduct
        this.fetchProducts(); // Fetch updated products list
      },
      (error: any) => {
        console.error('Error updating product:', error);
      }
    );
  }

  cancelEdit(): void {
    this.editingProduct = null; // Clear the editingProduct
  }
}
