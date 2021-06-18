from django.shortcuts import render,redirect
from address.models import Address

# Create your views here.
def home(requsest):
    return render(requsest, "address/index.html")
def list(request):
    # ----------------------------------------------------
    # select * from address_address
    #select count(*) from address_address
    #sql문을 사용할 수 있지만 보통은 함수로 호출해서 사용하는 것이 일반적
    # - Addressw.objects 레코드 주소
    # - order_by('') : 오름차순
    # - order_by('-') : 내림차순
    # ----------------------------------------------------
    items = Address.objects.order_by('name')

    #group 함수
    address_count = Address.objects.all().count()

    #이제 이 값을 url에 넘겨줘야지.
    return render(request, "address/addressList.html", {'items': items,
                                                        'address_count':address_count})
def write(request):
    return render(request, "address/addressWrite.html")

# form 파라미터 처리
def insert(request):
    # print("name :", request.POST['name'])

    # 데이터 베이스에 입력 처리 (idx 는 Oracle의 순번과 동일)
    addr = Address(name=request.POST['name'],
                   tel=request.POST['tel'],
                   email=request.POST['email'],
                   address=request.POST['address'],
    )
    addr.save()  # 레코드 추가

    # redirect 때는 /로 절대경로 설정해주어야함.
    return redirect("/address/list".Address)
    ##### redirect의 수입을 위해 ctrl+space 하면 자동 수입됨 #####

#상세페이지
def detail(request):
    idv = request.GET['idx']
    #select * from address_address where idx = idv
    addr = Address.objects.get(idx=idv)
    return render(request,'address/detail.html',{'addr':addr})

# 삭제 기능
# csrf_protect는 csrf 방식을 검증한다.
# 앞으로 post 방식일 때는 반드시 사용을 원칙으로 한다.
def delete(request):
    idv = request.POST['idx']
    print("idx:", idv)
    # delete * from address_address where idx = idv
    # 선택한 데이터의 레코드가 삭제됨
    addr = Address.objects.get(idx=idv).delete()
    return redirect('/address/list')


# 수정 기능
def update(request):
    id = request.POST['idx']
    name = request.POST['name']
    tel = request.POST['tel']
    email = request.POST['email']
    address = request.POST['address']

    print("idx:", id)
    print("name:", name)
    print("tel:", tel)
    print("email:", email)
    print("address:", address)
# 수정 데이터 베이스 처리(idx=id -> 값을 넣으면 수정, 없으면 auto로 생성되므로 없어도됨)
    addr = Address(idx=id, name=name, tel=tel, email=email, address=address)

    # 데이터 레코드가 수정됨
    addr.save()

    return redirect('/address/list')