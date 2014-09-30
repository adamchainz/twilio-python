from .. import InstanceResource, ListResource


class Reservation(InstanceResource):
    """
    A Reservation resource
    """

    def update(self, **kwargs):
        """
        Update a reservation.

        :param worker_activity_sid: Either accepted or rejected. Specifying
            accepted means the Worker has received the Task and will process
            it. Work Distribution Service will no longer consider this task
            eligible for assignment, and no other Worker will receive this
            Task. Specifying rejected means the Worker has refused the
            assignment and Work Distribution Service will attempt to assign
            this Task to the next eligible Worker.
        :param reservation_status: If rejecting a reservation, change the
            worker that is tied to this reservation to the supplied activity.
            If not provided, the WorkerPreviousActivitySid on the Reservation
            will be used.
        """
        return self.parent.update_instance(self.name, kwargs)


class Reservations(ListResource):
    """ A list of Reservation resources """

    name = "Reservations"
    instance = Reservation

    def update(self, sid, **kwargs):
        """
        Update a :class:`Reservation` with the given parameters.

        :param sid: Reservation sid to update.
        :param worker_activity_sid: Either accepted or rejected. Specifying
            accepted means the Worker has received the Task and will process
            it. Work Distribution Service will no longer consider this task
            eligible for assignment, and no other Worker will receive this
            Task. Specifying rejected means the Worker has refused the
            assignment and Work Distribution Service will attempt to assign
            this Task to the next eligible Worker.
        :param reservation_status: If rejecting a reservation, change the
            worker that is tied to this reservation to the supplied activity.
            If not provided, the WorkerPreviousActivitySid on the Reservation
            will be used.
        """
        return self.update_instance(sid, kwargs)
