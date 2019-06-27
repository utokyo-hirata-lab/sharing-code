program main
  use mtmod
  implicit none
  integer,parameter :: N = 10000000
  integer,parameter :: seed = 3
  real(8) :: x.y, pi
  integer :: i, counter
  
  call sgrnd(seed)

  counter = 0
  do i = 1, N
     x = grand()
     y = grand()
     if(x**2+y**2<1.d0) then
        counter = counter + 1
     endif
  enddo
