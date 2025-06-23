from django.shortcuts import render, HttpResponse
from ultralytics import YOLO
import cv2
from inventory.models import Product
from django.shortcuts import get_object_or_404

def out_of_stock(request):
    if request.method == 'GET':
        model = YOLO('yolov8n.pt')
        banana_product = get_object_or_404(Product, name="Banana")
        if banana_product.quantity_remaining > 0:
            banana_product.quantity_remaining -= 1
            qty = banana_product.quantity_remaining
            banana_product.save()
            message = "Banana quantity decreased successfully."
        else:
            message = "No bananas left in stock."
        print(message)
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            results = model(frame, show=True)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()
        return render(request, 'out_of_stock.html')
    else:
        return render(request, 'out_of_stock.html')