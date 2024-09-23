class Solution:
    def getIntersectionNode(self, headA, headB):

        #breute force 

        # tempA = headA
        # tempB = headB
        # lengthA = 0
        # while tempA:
        #     lengthA+=1
        # lengthB = 0
        # while tempB:
        #     lengthB+=1

        # tempA = headA
        # tempB = headB
        # if lengthA>lengthB:
        #     while lengthA>lengthB:
        #         tempA = tempA.next
        #         lengthA-=1
        # elif lengthB>lengthA:
        #     while lengthB>lengthA:
        #         tempB = tempB.next
        #         lengthB-=1
        # else:
        #     pass
        
        # out = tempA
        # while tempA:
        #     if tempA != tempB:
        #         out = out.next
        #     tempA = tempA.next
        #     tempB = tempB.next
        # return out ## time out 
        
        #hash set
        # st = set()
        # temp_a = headA
        # while temp_a:
        #     st.add(temp_a)
        #     temp_a = temp_a.next

        # temp_b = headB
        # while temp_b:
        #     if temp_b in st:
        #         return temp_b
        #     else:
        #         temp_b=temp_b.next
        # return None

        # super elegant solution
        temp_a = headA
        temp_b = headB

        while temp_a!=temp_b:
            temp_a = temp_a.next if temp_a else temp_a=headB
            temp_b = temp_b.next if temp_b else temp_a=headA

        return temp_a