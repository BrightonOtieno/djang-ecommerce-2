from django.urls import path,include
from .views import(
    ProductListView,
    ProductDetailView,
    add_to_cart,
    remove_from_cart,
    OrderSummaryView,
    remove_single_item_from_cart,
    CheckoutView,
    PaymentView,
    AddCoupon,
    RefundRequestView
)
urlpatterns = [
    path('', ProductListView.as_view(),name = "item-list"),
    path('product/<pk>/',ProductDetailView.as_view(),name = "product-detail"),
    path('order-summary/',OrderSummaryView.as_view(),name = "order-summary"),
    path('product/<slug>/add-to-cart',add_to_cart,name = "add-to-cart"),
    path('product/<slug>/remove-single-item',remove_single_item_from_cart,name = "remove-single-item"),
    path('product/<slug>/remove-from-cart',remove_from_cart,name = "remove-from-cart"),
    path('checkout/', CheckoutView.as_view(),name = "checkout"),
    path('add-coupon/', AddCoupon.as_view(),name = "add-coupon"),
    path('payment/<payment_option>/', PaymentView.as_view(),name = "payment"),
    path('request-refund/', RefundRequestView.as_view(),name = "request-refund"),

]
