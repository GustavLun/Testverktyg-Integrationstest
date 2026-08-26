# 1 Diskussion
Skapa en egen uppgift som handlar om att skriva integrationstest. Uppgiften ska träna på det vi gått igenom på lektionen:
- integrationstest
- markers
- (gärna spy också)

### I denna uppgift skall vi testa integration i vårat bowling system.
Klasser:
- Member (Förvarar ``name``och ``email``)
---
- Rental_Items (Innehåller en lista med tillgängliga bowlingklot och skor ``item``)
  - ``def add_item``
  - ``def rent_item``
---
- item (``item_name``, ``size``, ``amount``)
---
- Booking_System (System som innehåller ``Lanes``, ``time_slots``, ``Member.name``, ``rental_items``)

  - ``def book_lane``
  
Vi kan testa Rental_Items med units tests, vi kan även mocka när vi skall testa Booking_System. Men Vill vi testa med integration testing så kommer detta ske när vi officiellt vill testa Booking_System efter som den kommunicerar med Rental_Items.
    
